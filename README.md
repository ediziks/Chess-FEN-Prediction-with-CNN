# Chess-FEN-Prediction-with-CNN

This is a vision AI application through CNN (Convolutional Neural Network) that understands FEN positions of the
given chess board by looking at it. One of the methods to solve solving this problem is to use a CNN that is fed by
the chess board blocks divided into 64 squares represents alternative positions or pieces. In order to obtain the
findings, we first encode the labels into classes, and then decoding the outcomes to recreate the images with
expected FEN codes.

A common notation for defining a certain chess board position is the Forsyth-Edwards Notation (FEN). The goal of
FEN is to offer all the information required to restart a game from a specific point. By the time of now, researchers
who study machine learning have shown that it is possible to correctly guess a chess player's identity based on the
sequence of positions from their chess games. The method utilized in the study has the potential to be widely used
for identifying people based on a variety of activities.

CNN is a deep learning method that can take in an input picture, assign importance to various characteristics and
objects in the image, and distinguish between them. In comparison to other classification methods, a convolutional
network requires substantially less preprocessing. Convolutional networks can also learn these filters and attributes
with enough training, unlike basic approaches where filters must be manually engineered.

### To run the app:
- `pip install requirements.txt`
- `streamlit run app.py --server.port 8501`

### Screenshot

This is a sample image of the application predicting the FEN of a chess board

<img width="1212" alt="image" src="https://user-images.githubusercontent.com/54022220/183226204-487e0a2b-3fe1-47dc-893e-89745d81c09b.png">


P.S.: This application is has not been tested on platforms other than MacOS
