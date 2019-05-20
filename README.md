#CAR MODEL AND LICENSE PLATE RECOGNITION

This repository is to do car recognition by fine-tuning ResNet-152 with Cars Dataset from Stanford. And car license plate recognition using Open Cv 3.

## Dependencies

- Install Virtualenv
- Download the Repo
- Create a Virtualenv within the root directory
- Run [pip install -r requirements.txt]
- Also Download the res folder from (https://drive.google.com/open?id=185rYzipynJqPY9AXWaNAV9scnVMQudkC) for large resources needed for this project.


## Dataset

We use the Cars Dataset, which contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images, where each class has been split roughly in a 50-50 split.

 ![image](https://github.com/foamliu/Car-Recognition/raw/master/images/random.jpg)

You can get it from [Cars Dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html):


```bash
$ cd cpc
$ wget http://imagenet.stanford.edu/internal/car196/cars_train.tgz
$ wget http://imagenet.stanford.edu/internal/car196/cars_test.tgz
$ wget --no-check-certificate https://ai.stanford.edu/~jkrause/cars/car_devkit.tgz
```

- Extract the dataset and put them in a folder called data

## ImageNet Pretrained Models

Get [ResNet-152] from the res folder.

## Usage

### Data Pre-processing
Extract 8,144 training images, and split them by 80:20 rule (6,515 for training, 1,629 for validation):
```bash
$ python pre-process.py
```

### Train
```bash
$ python train.py
```

If you want to visualize during training, run in your terminal:
```bash
$ tensorboard --logdir path_to_current_dir/logs
```

 ![image] train.jpg in res folder

### Analysis
Update "model_weights_path" in "utils.py" with your best model, and use 1,629 validation images for result analysis:
```bash
$ python analyze.py
```

#### Validation acc:
**88.70%**

#### Confusion matrix:

 ![image] confusion_matrix.jpg in res folder

### Test
```bash
$ python test.py
```

Submit predictions of test data set (8,041 testing images) at [Cars Dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html), evaluation result:

#### Test acc:
**88.88%**

 ![image](https://github.com/foamliu/Car-Recognition/raw/master/images/test.jpg)

### Demo
Put [pre-trained model] model.96-0.89.hdf5 in res folder into "models" folder then run:

```bash
$ python demo.py --i [image_path]
```
If no argument, a sample image is used:

 ![image] 07647.jpg in res folder

```bash
$ python demo.py
class_name: Lamborghini Reventon Coupe 2008
prob: 0.9999994
```

#For License plate recognition
Run Python Main.py
- P.S put your image path into the image var in Main.py
