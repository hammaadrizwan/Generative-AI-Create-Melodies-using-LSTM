from preprocess import generate_training_sequences,SEQUENCE_LENGTH
import tensorflow.keras as keras

OUTPUT_UNITS=38
LOSS="sparse_categorical_crossentropy"
LEARNING_RATE=0.001
NUM_UNITS=[256]
EPOCHS=5
BATCH_SIZE=64
SAVE_MODEL_PATH="model.h5"

def build_model(output_units, loss, learning_rate, num_units):
    input = keras.layers.Input(shape=(None, output_units))
    x = keras.layers.LSTM(num_units[0])(input)
    x=  keras.layers.Dropout(0.2)(x)

    output=keras.layers.Dense(output_units, activation="softmax")(x)
    model=keras.Model(input, output)

    model.compile(loss=loss, optimizer=keras.optimizers.Adam(learning_rate), metrics=["accuracy"])

    model.summary()
    return model



def train():
    inputs, targets = generate_training_sequences(SEQUENCE_LENGTH)

    model=build_model(output_units=OUTPUT_UNITS, loss=LOSS,learning_rate=LEARNING_RATE, num_units=NUM_UNITS)

    model.fit(inputs, targets, epochs=EPOCHS, batch_size=BATCH_SIZE)
    model.save(SAVE_MODEL_PATH)

if __name__=="__main__":
    train()