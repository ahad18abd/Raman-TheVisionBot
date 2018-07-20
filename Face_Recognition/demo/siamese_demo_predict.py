import sys
sys.path.insert(0, '/home/epsilon/Young/ML/Face_Recog/keras-face/')

from keras_face.library.siamese import SiameseFaceNet


def main():
    fnet = SiameseFaceNet()

    model_dir_path = './models'
    image_dir_path = "./data/images"
    fnet.load_model(model_dir_path)

    database = dict()
    database["danielle"] = [fnet.img_to_encoding(image_dir_path + "/danielle.png")]
    database["younes"] = [fnet.img_to_encoding(image_dir_path + "/younes.jpg")]
    database["tian"] = [fnet.img_to_encoding(image_dir_path + "/tian.jpg")]
    database["andrew"] = [fnet.img_to_encoding(image_dir_path + "/andrew.jpg")]
    database["kian"] = [fnet.img_to_encoding(image_dir_path + "/kian.jpg")]
    database["dan"] = [fnet.img_to_encoding(image_dir_path + "/dan.jpg")]
    database["sebastiano"] = [fnet.img_to_encoding(image_dir_path + "/sebastiano.jpg")]
    database["bertrand"] = [fnet.img_to_encoding(image_dir_path + "/bertrand.jpg")]
    database["kevin"] = [fnet.img_to_encoding(image_dir_path + "/kevin.jpg")]
    database["felix"] = [fnet.img_to_encoding(image_dir_path + "/felix.jpg")]
    database["benoit"] = [fnet.img_to_encoding(image_dir_path + "/benoit.jpg")]
    database["arnaud"] = [fnet.img_to_encoding(image_dir_path + "/arnaud.jpg")]
    database["deepak"] = [fnet.img_to_encoding(image_dir_path + "/deepak.jpg")]
    database["momo"] = [fnet.img_to_encoding(image_dir_path + "/momo.jpg")]

    fnet.verify(image_dir_path + "/camera_0.jpg", "younes", database)
    fnet.verify(image_dir_path + "/camera_2.jpg", "kian", database)
    # fnet.verify(image_dir_path + "/test_deepak_1.jpg", "deepak", database)
    # fnet.verify(image_dir_path + "/test_momo_1.jpg", "momo", database)
    # fnet.verify(image_dir_path + "/test_momo.jpg", "deepak", database)
    fnet.who_is_it(image_dir_path + "/camera_0.jpg", database)
    fnet.who_is_it(image_dir_path + "/younes.jpg", database)
    # fnet.who_is_it(image_dir_path + "/test_deepak_2.jpg", database)
    # fnet.who_is_it(image_dir_path + "/test_momo_2.jpg", database)


if __name__ == '__main__':
    main()