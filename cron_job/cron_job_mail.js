const nodemailer = require('nodemailer');

async function getReportingManagerEmail(employeeIds) {
  try {
    // Perform database query and retrieve the reporting manager's email based on each employeeId
    // Replace this with your actual database query logic

    // For demonstration purposes, let's assume you have a function to get the reporting manager's email:
    async function getReportingManagerEmailById(employeeId) {
      // Perform the database query here and return the reporting manager's email
      // Replace this with your actual database query logic
      // Example: const reportingManagerEmail = await queryReportingManagerEmailById(employeeId);
      // For now, we'll return a fixed email for demonstration purposes:
      return 'arvind3@ncircletech.com';
    }

    const reportingManagerEmails = await Promise.all(employeeIds.map(getReportingManagerEmailById));

    console.log("reportingManagerEmails:", reportingManagerEmails);
    return reportingManagerEmails;
  } catch (err) {
    console.error("Error:", err);
    return [];
  }
}


const nodemailer = require('nodemailer');

// ... Other route handlers and setup code ...

// Inside the main route handler
router.get('/week-record', async (req, res) => {
  try {
    // ... Your existing logic to fetch data ...

    // Get the employeeIds from the data object (assuming it's an array of objects)
    const employeeIds = data.map((item) => item.employeeId);

    // Get reporting manager emails for each employeeId
    const reportingManagerEmails = await getReportingManagerEmail(employeeIds);

    // ... Your existing logic ...

    // Send emails to reporting managers
    if (reportingManagerEmails.length > 0) {
      // Set up nodemailer transport
      const transporter = nodemailer.createTransport({
        // Set up your email transport configuration here (SMTP settings, etc.)
      });

      for (const email of reportingManagerEmails) {
        const mailOptions = {
          from: 'your-email@example.com',
          to: email,
          subject: 'Notification from Cron Job',
          text: 'This is a notification email sent from the cron job.'
        };

        try {
          // Send the email
          await transporter.sendMail(mailOptions);
          console.log(`Email sent to ${email}`);
        } catch (err) {
          console.error('Error sending email:', err);
        }
      }
    }

    // ... Your existing logic ...

    res.json({ status: 'ok', data });
  } catch (e) {
    res.json({ status: 'error', message: "Can't get details", error: e });
  }
});
