from image_processing.utils import io.plot
from image_processing.processing import combination, transformation
image1 = io.read_image("C:Users/Johnson/nft/nft1/monkey.jpg")
image2 = io.read_image("C:Users/Johnson/nft/nft1/monkey1.jpg")

plot.plot_image(image1)
plot.plot_image(image2)

result_image = combination.transfer_histogram(image1, image2)
plot.plot_result(image1, image2, result_image)