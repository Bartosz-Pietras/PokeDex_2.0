import numpy as np
import cv2 as cv
from PIL import Image

from flask import Flask, render_template, url_for, flash, redirect, request
from forms import PokemonImageForm
from tensorflow import keras
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a7eef72c6d1dadaed8be192c9dd1fb1a'

model = keras.models.load_model("my_model1")


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PokemonImageForm()
    if form.validate_on_submit():
        pokemon_pic = Image.open(form.pokemon.data)
        image = pokemon_pic.resize((224, 224))
        image = np.array(image)
        image = keras.applications.vgg16.preprocess_input(image)
        input_arr = keras.preprocessing.image.img_to_array(image)
        input_arr = np.array([input_arr])

        predictions = np.round(model.predict(input_arr))

        if predictions[0][0] == 1:
            pokemon = "Bulbasaur"
        elif predictions[0][1] == 1:
            pokemon = "Charmander"
        elif predictions[0][2] == 1:
            pokemon = "Pikachu"
        elif predictions[0][3] == 1:
            pokemon = "Squirtle"

        return redirect(url_for('result', pokemon=pokemon))
    return render_template('upload.html', title='Upload', form=form)


@app.route('/result')
def result():
    pokemon = request.args.get('pokemon')
    return render_template('result.html', title='Result', pokemon=pokemon)


if __name__ == '__main__':
    app.run()
