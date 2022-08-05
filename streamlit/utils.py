from skimage import io, transform
from skimage.util.shape import view_as_blocks
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def process_image(img):
    downsample_size = 200
    square_size = int(downsample_size/8)
    img_read = io.imread(img)
    img_read = transform.resize(
      img_read, (downsample_size, downsample_size), mode='constant')
    tiles = view_as_blocks(img_read, block_shape=(square_size, square_size, 3))
    tiles = tiles.squeeze(axis=2)

    return tiles.reshape(64, square_size, square_size, 3)


def fen_from_onehot(one_hot):
    piece_symbols = 'prbnkqPRBNKQ'
    output = ''
    for j in range(8):
        for i in range(8):
            if(one_hot[j][i] == 12):
                output += ' '
            else:
                output += piece_symbols[one_hot[j][i]]
        if(j != 7):
            output += '-'

    for i in range(8, 0, -1):
        output = output.replace(' ' * i, str(i))

    return output


def load_model(model_path):
    from keras.models import load_model
    return load_model(model_path)


def predicted_fen_plot(image):
    plt.figure(figsize=(5, 5))
    model = load_model('../model.h5')
    pred = model.predict(process_image(image)).argmax(axis=1).reshape(-1, 8, 8)
    fen = fen_from_onehot(pred[0])
    imgplot = plt.imshow(mpimg.imread(image))
    plt.axis('off')
    plt.title(fen)
    plt.show()