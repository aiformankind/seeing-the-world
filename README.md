# Seeing the World

> ***If an autonomous vehicle can drive itself, I strongly believe we can enable the vision impaired and blinds to see and navigate the world with ease.***


Enabling the vision impaired and blinds to see and navigate the world with ease is the main goal of this AI for Mankind's **Seeing the World** open source project. We want to leverage the power of open source community to build low cost open source image recognition and object detection models to empower the vision impaired and blinds to see and navigate the world. All the models built will be freely available to all across the entire world.

According to WHO, there are 253 million people live with vision impairment. 217 million have moderate to severe vision impairment and 36 million are blind. 81% of people who are blind or have moderate or severe vision impairment are aged 50 years and above.

### List of Projects

#### Image Recognition
- Farmer Market

>As a baby step, we will start with building model to recognize fruit and vegetable in Farmer Market and expand to other settings. We will contribute back all the models back to Microsoft Seeing AI [Microsoft's Seeing AI app](https://www.microsoft.com/en-us/seeing-ai)

>We encourage our members and public to take pictures of different fruit and vegetable whenever they go to Farmer Market and commit back to the repo. We will build model using these pictures.

- Hotel


#### Object Detection
- Outdoor Space Detection
- Indoor Space Detection

#### Quick Start

**Building Fruit/Vegetable Model via Transfer Learning**

Install Docker:

https://docs.docker.com/v17.12/docker-for-mac/install/#install-and-run-docker-for-mac

We use the scripts provided by the following excellent Google’s TensorFlow For Poets codelab.
https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0

Clone the repo:
```
https://github.com/aiformankind/seeing-the-world.git
```
Go to the repo directory:
```
cd seeing-the-world
```
Start Tensorflow docker:
```
docker run -it --rm -p 8888:8888 -v $PWD:/work -w /work tensorflow/tensorflow bash
```
Set environment variables:
```
IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"
```

Install Augmentor:
https://github.com/mdbloice/Augmentor
```
apt update
apt install wget
pip install Augmentor
```

Augment data:
```
python augment/augment_images.py
```

Retrain model:
```
python -m train.retrain   --bottleneck_dir=train_output/bottlenecks   --how_many_training_steps=500   --model_dir=train_output/models/   --summaries_dir=train_output/training_summaries/"${ARCHITECTURE}"   --output_graph=train_output/retrained_graph.pb   --output_labels=train_output/retrained_labels.txt   --architecture="${ARCHITECTURE}" --image_dir=augment-data
```
Predict label:

```
python -m train.label_image --graph=train_output/retrained_graph.pb --image=validation/eggplant/eggplant-harvest-basket.jpg
```
#### Project Advisors:
Jigar Doshi from CrowdAI

