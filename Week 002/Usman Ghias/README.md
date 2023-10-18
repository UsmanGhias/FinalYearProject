# ChatBot using Python and Tkinter

## Project Overview

Welcome to the ChatBot project! This project aims to create a simple yet interactive chatbot using Python and the Tkinter library for the graphical user interface (GUI). The chatbot is designed to understand user input, predict intents, and generate contextually relevant responses. It serves as a foundation for building conversational interfaces and can be extended with more sophisticated natural language processing (NLP) techniques.

## Project Structure

The project is organized into several components, each with a specific role:

1. **ChatBot Model**: The heart of the chatbot, responsible for predicting user intents and generating responses. The model is trained using a predefined dataset of intents and responses.

2. **Data**: Contains the JSON file ('intents.json') used for training the chatbot model. This file defines the intents, patterns, and responses that the chatbot understands.

3. **Preprocessing**: Preprocessing tasks include tokenization and lemmatization. The 'nltk' library is used for these tasks, making the text data suitable for model training.

4. **Graphical User Interface (GUI)**: The chatbot's user interface is built using the Tkinter library. It includes a chat window, a message input box, and a "Send" button for user interactions.

5. **Interaction Functions**: Several functions manage user interactions, such as sending messages, predicting intents, and generating responses. These functions enable the chatbot to engage in conversations.

6. **Main Application ('app.py')**: The main application file where the chatbot's GUI is initialized and the main loop is run. Users interact with the chatbot through this application.

## Getting Started

Follow these steps to get started with the chatbot:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/usmanghias/tensor_chatbot.git
    ```

2. **Install Dependencies**: Ensure you have the required Python libraries installed. You can install them using 'pip':

    ```
    pip install numpy keras tensorflow nltk pickle
    ```

3. **Run the ChatBot**: Run the chatbot application by executing 'app.py'. This will open the GUI where you can chat with the bot.

    ```
    python train_chatbot.py
    ```

4. **Chat with the Bot**: Start typing messages in the input box and click the "Send" button to engage in a conversation with the chatbot.

## Extending the ChatBot

You can extend and improve the chatbot by:

- Training the model with a more extensive dataset to improve intent recognition.
- Implementing more advanced NLP techniques for better responses.
- Adding additional features, such as user authentication, external integrations, or voice recognition.

Feel free to explore and experiment with the code to make the chatbot more powerful and engaging.

## Acknowledgments

- The project was created with inspiration from various online resources and tutorials.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy chatting with your chatbot! 🤖
