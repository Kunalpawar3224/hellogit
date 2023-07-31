// let value = 1;

// doSomething= () => {
//     console.log("kmv")
//   value = 2;
// };

// console.log(value);
// doSomething()


//////////Synchronous Callback //////////////
// function CallBackTeaser(callback, param){
//     console.log("Calling the callback function")
//     callback(param);
//     console.log("callback function excecution completed")
//     }
//     function consoleMyDetails(person){
//     if(person){
//     console.log(`Hi, my name is ${person.name}, i am ${person.job} & super exited about ${person.hobby}`);
//     }
//     }
//     CallBackTeaser(consoleMyDetails, {'name': 'Praveen',
//     'job':'Developer',
//     'hobby':'learning new technologies.'
//     });

    

//////////Asynchronous Callback //////////////

function CallBackTeaser(callback, param){
    console.log(`Calling the callback function`);
    setTimeout(()=>{callback(param)}, 0);//Calling the function asynchronously, passing the callback function as the first argument
    console.log(`callback function completed execution`);
    }
    function consoleMyDetails(person){
    if(person){
    console.log(`Hi, my name is ${person.name}, i am ${person.job} & super exited about ${person.hobby}`);
    }
    }
    CallBackTeaser(consoleMyDetails, {'name': 'Praveen',
    'job':'Developer',
    'hobby':'learning new technologies.'
    });