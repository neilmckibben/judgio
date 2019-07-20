document.addEventListener('click', function (event) {
  console.log('It workds');
  if (event.target.matches('#id_new_hackers')){
    var label = document.getElementById('id_new_hackers');
    var val = label.options[label.selectedIndex].text;

    var formThreeName = document.getElementById("id_member_three_name");
    var formThreeEmail = document.getElementById("id_member_three_email");
    var formFourName =   document.getElementById("id_member_four_name");
    var formFourEmail = document.getElementById("id_member_four_email");
    if(val == 2){
      Console.log(2);
      formThreeName.disabled = true;
      formThreeEmail.disabled = true;
      formFourName.disabled = true;
      formFourEmail.disabled = true;
    }
    else if(val == 3){
      formThreeName.disabled = false;
      formThreeEmail.disabled = false;
      formFourName.disabled = true;
      formFourEmail.disabled = true;
    }
    else if(val == 4){
      formThreeName.disabled = false;
      formThreeEmail.disabled = false;
      formFourName.disabled = false;
      formFourEmail.disabled = false;
    }
  }
}, false);
