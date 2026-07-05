import cv2
import numpy as np


# 构建高斯金字塔
def gaussian_pyramid(image, levels):
    gaussian_pyramid = [image]
    for i in range(levels - 1):
        image = cv2.pyrDown(image)
        gaussian_pyramid.append(image)
    return gaussian_pyramid


# 构建拉普拉斯金字塔
def laplacian_pyramid(gaussian_pyramid):
    laplacian_pyramid = []
    for i in range(len(gaussian_pyramid) - 1):
        next_gaussian = cv2.pyrUp(gaussian_pyramid[i + 1],
                                  dstsize=(gaussian_pyramid[i].shape[1], gaussian_pyramid[i].shape[0]))
        laplacian = cv2.subtract(gaussian_pyramid[i], next_gaussian)
        laplacian_pyramid.append(laplacian)
    laplacian_pyramid.append(gaussian_pyramid[-1])  # 添加最后一层的高斯图像
    return laplacian_pyramid


# 混合多个图像的拉普拉斯金字塔
def blend_pyramids_multiple(laplacian_pyramids, mask_pyr, weights):
    blended_pyramid = []
    for l in range(len(laplacian_pyramids[0])):  # 假设每个金字塔有相同的层数
        blended_layer = np.zeros_like(laplacian_pyramids[0][l], dtype=np.float32)
        total_weight = 0
        for i in range(len(laplacian_pyramids)):  # 对每个图像的层进行加权
            weight = weights[i]
            blended_layer += laplacian_pyramids[i][l] * weight
            total_weight += weight
        blended_layer /= total_weight  # 归一化
        blended_pyramid.append(blended_layer)
    return blended_pyramid


# 重建图像
def reconstruct_from_pyramid(laplacian_pyramid):
    image = laplacian_pyramid[-1]
    for i in range(len(laplacian_pyramid) - 2, -1, -1):
        image = cv2.pyrUp(image, dstsize=(laplacian_pyramid[i].shape[1], laplacian_pyramid[i].shape[0]))
        image = cv2.add(image, laplacian_pyramid[i])
    return image


# 主函数：处理n幅图像和掩模图像
def laplacian_pyramid_blending_multiple(images, mask, weights, levels=5):
    # 构建多个图像的高斯和拉普拉斯金字塔
    gaussian_pyramids = [gaussian_pyramid(image, levels) for image in images]
    laplacian_pyramids = [laplacian_pyramid(gaussian_pyramid) for gaussian_pyramid in gaussian_pyramids]
    # 构建掩模图像的高斯金字塔
    mask_gaussian_pyr = gaussian_pyramid(mask, levels)

    # 将掩模二值化以便用于混合
    mask_gaussian_pyr = [m.astype(np.float32) / 255 for m in mask_gaussian_pyr]

    # 混合拉普拉斯金字塔
    blended_pyramid = blend_pyramids_multiple(laplacian_pyramids, mask_gaussian_pyr, weights)

    # 从混合的拉普拉斯金字塔重建最终图像
    blended_image = reconstruct_from_pyramid(blended_pyramid)

    return blended_image


# 选择图像并生成随机权重
images = []
weights = []


def img_select(n):
    global images, weights
    for i in range(n):
        image = cv2.imread(f'../3.20_testImage/input_{i + 1}.png')
        if image is None:
            print(f"图像 {i + 1} 加载失败")
            continue
        image = cv2.resize(image, (128, 128))  # 确保图像大小一致
        images.append(image)

    # 生成随机权重并归一化
    weights = np.random.rand(n)
    weights /= np.sum(weights)  # 归一化


# 设置掩模，生成渐变掩模
height, width = 128, 128  # 获取图像的尺寸
mask = np.zeros((height, width), dtype=np.uint8)
for i in range(width):
    mask[:, i] = int((i / width) * 255)  # 从左到右渐变
cv2.imwrite('../3.20_testImage/mask.jpg', mask)

# 确保掩模是三通道图像
mask = np.stack([mask] * 3, axis=-1)  # 将单通道掩模扩展为三通道

# 选择图像和权重
img_select(4)

# 调用多图像金字塔融合函数
result = laplacian_pyramid_blending_multiple(images, mask, weights, levels=5)
if result is not  None:
    print(f'处理成功，融合了{len(images)}张图片')
else:
    print('处理失败')
# 保存融合后的图像
cv2.imwrite(f'../3.20processImage/blended_image_{len(images)}.jpg', result)
