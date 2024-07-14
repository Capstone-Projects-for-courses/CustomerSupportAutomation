# Customer Support AI

This project uses a fine-tuned GPT-2 model to automate customer support interactions. The application allows users to ask questions and receive responses from the AI.

## Features

- Automated responses to customer queries
- Web interface for interacting with the AI
- Flask backend to handle requests and responses

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- Anaconda (recommended for managing environments)
- Git

### Setup

1. **Clone the repository**

    ```bash
    git clone https://github.com/Capstone-Projects-for-courses/CustomerSupportAutomation
    cd CustomerSupportAutomation
    ```

2. **Create and activate a virtual environment**

    Using the provided Conda environment file:

    ```bash
    conda env create -f environment.yml
    conda activate capstoneProject
    ```

3. **Download and fine-tune the GPT-2 model**

    Ensure you have the `customer_support_data_large.csv` for training. Run the fine-tuning script:

    ```bash
    python model_fine_tuning.py
    ```

## Running the Application

1. **Start the Flask application**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to**

    ```
    http://127.0.0.1:5001/
    ```

3. **Interact with the AI**

    - Enter a query in the input field and click the "Get Response" button.
    - The AI-generated response will be displayed below the input field.


## Video

[![Watch the video](https://github.com/Capstone-Projects-for-courses/CustomerSupportAutomation/blob/main/test.png)](https://github.com/Capstone-Projects-for-courses/CustomerSupportAutomation/blob/main/test.mp4)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
