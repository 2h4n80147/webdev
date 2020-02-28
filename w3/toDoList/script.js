function addRow(){
	var table = document.getElementById("tasks");
	var row = table.insertRow();
	var cell = row.insertCell();
	var input = document.getElementById("task_text");
	cell.innerHTML = `
	<label class="container">
		<input class="checkbox" type="checkbox">
		<span class="checkmark"></span>
	</label>
	` + '<p class="row_text">' 
	+ input.value 
	+ "</p>" 
	+ '<button class="delete_button" onclick="deleteRow(this)"><i class="material-icons" style="color:red">delete_outline</i></button>';
	input.value = "";
}

function deleteRow(x){
	var row = x.parentElement.parentElement;
	row.parentElement.removeChild(row);
	var table = document.getElementById("tasks");
	for(var i = 0; i < table.rows.length; ++i){
		var row = table.rows[i];
		var cell = row.cells[0];
		if(cell.querySelector('.checkbox').checked){
			row.parentElement.removeChild(row);
			--i;
		}
	}
}

function handleKeypress(e){
	e = e || window.event;
	if(e.keyCode == 13){
		e.preventDefault();
		document.getElementById("task_button").click();
		return false;
	}
	return true;
}