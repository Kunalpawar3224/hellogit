const cron = require('node-cron');

// Function to be executed by the cron job
function myTask() {
  console.log('Cron job is running at 8 am daily!');
  // Add your task logic here
}

// Set up the cron job to run daily at 8 am
// The cron expression format is: minute hour dayOfMonth month dayOfWeek
// To run at 8 am daily: '0 8 * * *' (0th minute, 8th hour, every day of the month, every month, every day of the week)
cron.schedule('0 8 * * *', myTask);

console.log('Cron job scheduled. Waiting for execution...');



router.get('/week-record', async (req, res) => {
  try {
    const today = new Date();
    const currentDay = today.getDay();

    const startofweek = new Date(today.setDate(today.getDate() - today.getDay()));
    const startOfWeek = new Date(
      Date.UTC(startofweek.getUTCFullYear(), startofweek.getUTCMonth(), startofweek.getUTCDate())
    );

    if (currentDay >= 2) {
      const weekdays = ["mon", "tue", "wed", "thu", "fri"];
      const i = currentDay - 2;

      const startOfWeekUTC = new Date(
        Date.UTC(startOfWeek.getUTCFullYear(), startOfWeek.getUTCMonth(), startOfWeek.getUTCDate())
      );

      const wed = await TimeSheet.find({
        "WeekRecord": {
          "$elemMatch": {
            "startDate": {
              "$gte": startOfWeekUTC,
              "$lte": new Date(startOfWeekUTC.getTime() + 24 * 60 * 60 * 1000)
            },
            [weekdays[i]]: 0
          }
        }
      },
      "employee project"
      );

      const data = await Promise.all(
        wed.map(async (obj) => {
          try {
            const emp = await Employee.findById(obj.employee);
            const proj = await Project.findById(obj.project);

            return { employeeEmail: emp ? emp.email : "Employee not found", projectName: proj ? proj.name : "Project not found" };
          } catch (err) {
            console.error("Error:", err);
            return { employeeEmail: "Error occurred", projectName: "Error occurred" };
          }
        })
      );

      // data now contains an array of objects with employeeEmail and projectName

      console.log("data is =", data);
      sendNotificationToReportingManager('64c0b545022s65df25592205b');
    } else {
      console.log("no zero's");
    }

    res.json({ status: 'ok', data });
  } catch (e) {
    res.json({ status: 'error', message: "Can't get details", error: e });
  }
});
