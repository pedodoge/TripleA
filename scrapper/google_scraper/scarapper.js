var myHeaders = new Headers();
myHeaders.append("apikey", "0A9A50E7hDk9QdAHXKe7mKAjHAnkbcup");

var requestOptions = {
    method: 'GET',
    redirect: 'follow',
    headers: myHeaders
};

fetch("https://api.apilayer.com/google_search?q=singapore%20crypto%20ownership", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));