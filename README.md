# Generative AI to create melodies using LSTM

## Overview
HarmonAI is a supervised Learning project that utilizes Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM) networks to generate original melodies. This project explores the capabilities of deep learning models in the field of music composition, enabling the creation of unique and harmonious musical pieces.

## Features
- **RNN and LSTM Networks**: Utilizes both RNN and LSTM architectures for melody generation, leveraging their ability to capture sequential patterns in music.
- **Original Melody Generation**: Generates new, original melodies based on input data and learned patterns, offering endless possibilities for musical exploration.
- **Customizable Parameters**: Allows users to adjust various parameters such as sequence length, number of layers, and training epochs to fine-tune the melody generation process.
- **MIDI Output**: Provides output in MIDI format, making it easy to listen to and further manipulate generated melodies using music software.

## Why RNN and LSTM?

Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM) networks are particularly well-suited for sequential data generation tasks like melody composition. Here's why we chose to utilize RNN and LSTM architectures for the MelodyGen project:

### 1. Capturing Long-Term Dependencies:
   - Melodies often exhibit long-term dependencies, where a note played at one point in the composition can have a significant impact on notes played much later. LSTM networks, with their ability to retain information over long sequences, are adept at capturing these dependencies, allowing for the generation of coherent and harmonious melodies.

### 2. Learning Sequential Patterns:
   - Music, being a temporal art form, relies heavily on sequential patterns and structures. RNNs, including LSTMs, excel at learning patterns in sequences of data. By training our models on a dataset of melodies, the RNN and LSTM networks can learn the underlying patterns and structures of music, enabling them to generate new melodies that adhere to these learned patterns while also exhibiting creativity and originality.

### 3. Flexible Architecture:
   - RNN and LSTM architectures offer flexibility in model design, allowing us to experiment with different network architectures, layer configurations, and hyperparameters to achieve optimal results. This flexibility enables us to tailor the model architecture to the specific requirements of melody generation and fine-tune the model's performance.

### 4. Musical Composition Suitability:
   - RNN and LSTM networks have been successfully applied to various tasks in music composition, including melody generation, chord progression prediction, and music transcription. Their proven effectiveness in generating high-quality musical outputs makes them ideal candidates for our MelodyGen project, where the goal is to create original and compelling melodies.

In summary, RNN and LSTM networks provide the necessary tools and capabilities to tackle the challenges of melody generation, making them the natural choice for the MelodyGen project.
