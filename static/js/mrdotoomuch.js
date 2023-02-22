$(document).ready(function(){
    $("#query").submit(function(event) {
        var valid = true;
        if($("[name=dinnie]").val() == '') {
            valid = false;
            alert("error, la fecha de incio esta vacia");
        }
        if($("[name=dinnie]").val() == '') {
            valid = false;
            alert("error, la fecha de incio esta vacia");
        }
        var dinnie = new Date($("[name=dinnie]").val());
        var finnie = new Date($("[name=finnie]").val());
        if(finnie<dinnie) {
            alert("la fecha de inicio debe de ser anterior a la de fin");
            valid = false;
        }
        if(!valid)
            event.preventDefault();
        });
});
