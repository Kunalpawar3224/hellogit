const axios = require('axios');

// Function to be executed by the cron job
async function myTask() {
  try {
    const response = await axios.get('http://localhost:3000/week-record'); // Make a GET request to your API endpoint
    const matchingDates = response.data; // Assuming the API returns the relevant data

    // Handle the matchingDates data as needed
    console.log('Matching dates:', matchingDates);

    // Rest of the existing route handling logic...
    // You can place the remaining code here.

    // If you need to call other functions, you can do so within the myTask() function.

    // Example:
    // const result = await someOtherFunction();

    // Send notifications or perform other actions here based on the data obtained from matchingDates.

    // Remember that you can't directly use res.send() inside a cron job function,
    // as there is no HTTP response context here. Instead, you can log or process the data as needed.
  } catch (error) {
    console.error('Error occurred during the cron job:', error.message);
  }
}

// Set up the cron job to run daily at 8 am
cron.schedule('0 8 * * *', myTask);

console.log('Cron job scheduled. Waiting for execution...');
