function basic(username, password) {
	return btoa(username + ":" + password)
}

var lock = false;
var token = "";

$(document).ready(function() {

	$('#openlogin').click(function() {
		$('.mdl-layout__drawer').addClass('is-visible');
	});

	// Sidebar functions
	/*$('#login').click(function(){
		// Check if connecting already
		if (lock) {
			return;
		}
		lock = true;
		try {
			var connection = $.ajax('/login', {
				beforeSend: function(item) {
					item.setRequestHeader("Authorization", "Basic " + basic($('#username').value, $('#password').value));
				},
				success: function(data) {
					// Store token from base64
					token = atob(data);
					return;
				}
			});
		} catch (e) {
			// What to do here?
		} finally {
			lock = false;
		}
		return;
	});
	
	$('#signup').click(function(){
		return;
	});*/

});
