function villagers(){
	var mail=document.getElementById("email").value
	var pass=document.getElementById("pass").value
	axios({
		method: 'post',
		url: 'https://localhost:8000/details',
		data: {
			email : mail,
			password : pass,
		}
	}).then(response => {
		var store=response.data
	})
}
