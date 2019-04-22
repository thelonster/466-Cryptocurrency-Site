var BTCdata = [];
var ETHdata = [];
var XRPdata = [];
var BCHdata = [];
var LTCdata = [];
var XLMdata = [];
var ETCdata = [];
var BATdata = [];
var ZECdata = [];
var REPdata = [];

function getData() {
    var endpoint = 'api/multipledata'
    $.ajax({
        method: 'GET',
        url: endpoint,
        success : function(result) {
            //var jsonData = JSON.parse(result);
            console.log(result);
            var display = result.DISPLAY
            console.log(display)
            BTCdata = display.BTC.USD
            console.log(BTCdata)
            //fillData(result);
        },
        error: function(err_data) {
            console.log('error')
            console.log(err_data)
        }
    })
}

function fillData(data) {

}
