# Deploy-Diabetes-Prediction-Model
## Task
Write a code to deploy Diabetes Prediction model using **Streamlit**</br>
Tool Used: </br>
Anaconda Navigator, Spyder, Jupyter Notebook, Python
## Workflow
### Libraries:
Libraries needed to achieve the task:

- NumPy
- Pandas
- Pickle: Library used to save and load the model 
- Streamlit(pip install streamlit)

### Process
- Save the build model to a file in binary format using pickle's dump function
- Load the saved model.
- Create Function in **Spyder**
- First Function to do the prediction in which feature values are passed as argument
  1. Change the input data to numpy array and reshape it
  2. Do the prediction using the saved model and return the result
- Second function would the main function which contains the streamlit function to create a web interface:
  1. Create a title for the web page
  2. Get the input values(Feature/ Column name except the Target) from user using text_input function of Streamlit
  3. Create a Button which would call the function for prediction when clicked
  4. Print the result</br></br></br>
  
Reference: Deploy Machine Learning Model using Streamlit in Python | ML model Deployment, Siddhardhan, https://www.youtube.com/watch?v=WLwjvWq0GWA&list=PLfFghEzKVmjsNtIRwErklMAN8nJmebB0I&index=109
 
