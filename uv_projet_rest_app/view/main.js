let unPressed = [];
let notUnPressed = [];
let lastPressedTime = null;
let timeoutId = null;
let sendedDataLength = 0;
const waitingTime = 4000;

function get_key1_key2(keys_down, keys_up){
    tab = [];
    let i = 0
    number = {};
    nextnumber = {};
    console.log(keys_down.length);
    console.log(i);
    if(keys_down.length> 1){
        for(i=1; i < keys_down.length &&  i < keys_up.length; i++){
            try{

                if(!number[keys_down[i-1].key])
                    number[keys_down[i-1].key] = 0;
                if(!nextnumber[keys_down[i].key])
                    nextnumber[keys_down[i].key] = 0;
                if(keys_down[i-1].key == keys_down[i].key)
                    nextnumber[keys_down[i].key] += 1;

                nextnumber[keys_down[i].key] += 1;
                number[keys_down[i-1].key]+=1;
                console.log(keys_up[i-1].latest , keys_down[i-1].latest, keys_up[i-1].history[number[keys_down[i-1].key]*2-1].duration);
                //duration = 55;
                tab.push([keys_down[i-1].key, keys_down[i].key, keys_up[i-1].history[number[keys_up[i-1].key]*2-1].duration, 
                    -keys_down[i-1].history[number[keys_down[i-1].key]*2-2].timestamp + keys_down[i].history[nextnumber[keys_down[i].key]*2-2].timestamp,
                    -keys_down[i-1].history[number[keys_down[i-1].key]*2-2].timestamp + keys_down[i].history[nextnumber[keys_down[i].key]*2-1].timestamp, 
                    -keys_down[i-1].history[number[keys_down[i-1].key]*2-1].timestamp + keys_down[i].history[nextnumber[keys_down[i].key]*2-2].timestamp ,
                    -keys_down[i-1].history[number[keys_down[i-1].key]*2-1].timestamp + keys_down[i].history[nextnumber[keys_down[i].key]*2-1].timestamp   ]);
            }
            catch(e){
                console.log(keys_down[i-1], keys_down[i]);
                continue;
            }
            //tab. keys_down[i].key
        }
    }
    return tab;

}

function sendData(keys, userName){
  let newData = [];
  for(let j = sendedDataLength; j < keys.length; j++){
    newData.push(keys[j]);
  }

  data = {"userName": userName, "data": newData}
  let options = {
      method: 'POST',
      //mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    };
  return fetch("http://localhost:8000/keys", options)
      .then(response => {
          if (response.ok) {
            sendedDataLength = keys.length;
            return response.json();
          } else {
          throw new Error('Erreur lors de la requête');
          }
      })
      .then(data => {
          console.log('Succès :', data);
          return data
      })
      .catch(error => {
          console.error('Erreur :', error);
      });
}

function handleKeyboardEvent(e) {
    console.log(e);
  if (e.pressed == true) {
    unPressed.push(e);
    lastPressedTime = e.latest;
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      // Action à effectuer 5 secondes après la dernière occurrence
      console.log("Action déclenchée 5 secondes après la dernière occurrence");
      let = usernameTag = document.getElementById('continue-auth-username');
      if(usernameTag != undefined){
        let userName = usernameTag.innerText;
        if(userName.trim() != ""){
            let keys = get_key1_key2(unPressed, notUnPressed);
            sendData(keys, userName)
            console.log(keys);
        }
      }
      //unPressed = [];
      //notUnPressed = [];
      
      //tracker = new KeyboardTracker(handleKeyboardEvent, { history: true, persistence: false });
    }, waitingTime);
    
  } else {
    notUnPressed.push(e);
  }

  document.getElementById('data').innerText = JSON.stringify(unPressed);
}

let tracker = new KeyboardTracker(handleKeyboardEvent, { history: true, persistence: false });