<?php   

	function xor_encrypt($in, $key) {  
	    // $key = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));  
	    $text = $in;  
	    $outText = '';  
	  
	    // Iterate through each character  
	    for($i=0;$i<strlen($text);$i++) {  
	    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
	    }  
	  
	    return $outText;  
	}  
	  
	$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

	$plaintext = json_encode($defaultdata);
	$ciphertext = hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');

	$key = 'qw8J';
	$good_input = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
	
	$good_plaintext = json_encode($good_input);
	$good_ciphertext = xor_encrypt($good_plaintext, $key);

	$cookie = base64_encode($good_ciphertext);	
  	echo $cookie;
?>
