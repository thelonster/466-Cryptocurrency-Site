function getData() {
    var endpoint = 'api/multipledata'
    $.ajax({
        method: 'GET',
        url: endpoint,
        success : function(result) {
            fillData(result);
        },
        error: function(err_data) {
            console.log('error')
            console.log(err_data)
        }
    })
}

// fillData updates the coins and dashboard pages with the current price and
// trend data from cryptocompare
//
// data is a JSON object containing price and trend data of the coins
function fillData(data) {
    //console.log($("#btcpct").html())
    if (data.DISPLAY.BTC.USD.CHANGEPCT24HOUR > 0) {
        $("#BTCpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BTC.USD.CHANGEPCT24HOUR + "%")
        $("#BTCprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BTC.USD.PRICE)
    } else {
        $("#BTCpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BTC.USD.CHANGEPCT24HOUR + "%")
        $("#BTCprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BTC.USD.PRICE)
    }
    if (data.DISPLAY.ETH.USD.CHANGEPCT24HOUR > 0) {
        $("#ETHpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETH.USD.CHANGEPCT24HOUR + "%")
        $("#ETHprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETH.USD.PRICE)
    } else {
        $("#ETHpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETH.USD.CHANGEPCT24HOUR + "%")
        $("#ETHprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETH.USD.PRICE)
    }
    if (data.DISPLAY.XRP.USD.CHANGEPCT24HOUR > 0) {
        $("#XRPpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XRP.USD.CHANGEPCT24HOUR + "%")
        $("#XRPprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XRP.USD.PRICE)
    } else {
        $("#XRPpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XRP.USD.CHANGEPCT24HOUR + "%")
        $("#XRPprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XRP.USD.PRICE)
    }
    if (data.DISPLAY.BCH.USD.CHANGEPCT24HOUR > 0) {
        $("#BCHpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BCH.USD.CHANGEPCT24HOUR + "%")
        $("#BCHprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BCH.USD.PRICE)
    } else {
        $("#BCHpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BCH.USD.CHANGEPCT24HOUR + "%")
        $("#BCHprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BCH.USD.PRICE)
    }
    if (data.DISPLAY.LTC.USD.CHANGEPCT24HOUR > 0) {
        $("#LTCpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.LTC.USD.CHANGEPCT24HOUR + "%")
        $("#LTCprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.LTC.USD.PRICE)
    } else {
        $("#LTCpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.LTC.USD.CHANGEPCT24HOUR + "%")
        $("#LTCprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.LTC.USD.PRICE)
    }
    if (data.DISPLAY.XLM.USD.CHANGEPCT24HOUR > 0) {
        $("#XLMpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XLM.USD.CHANGEPCT24HOUR + "%")
        $("#XLMprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XLM.USD.PRICE)
    } else {
        $("#XLMpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XLM.USD.CHANGEPCT24HOUR + "%")
        $("#XLMprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.XLM.USD.PRICE)
    }
    if (data.DISPLAY.ETC.USD.CHANGEPCT24HOUR > 0) {
        $("#ETCpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETC.USD.CHANGEPCT24HOUR + "%")
        $("#ETCprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETC.USD.PRICE)
    } else {
        $("#ETCpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETC.USD.CHANGEPCT24HOUR + "%")
        $("#ETCprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ETC.USD.PRICE)
    }
    if (data.DISPLAY.BAT.USD.CHANGEPCT24HOUR > 0) {
        $("#BATpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BAT.USD.CHANGEPCT24HOUR + "%")
        $("#BATprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BAT.USD.PRICE)
    } else {
        $("#BATpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BAT.USD.CHANGEPCT24HOUR + "%")
        $("#BATprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.BAT.USD.PRICE)
    }
    if (data.DISPLAY.ZEC.USD.CHANGEPCT24HOUR > 0) {
        $("#ZECpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZEC.USD.CHANGEPCT24HOUR + "%")
        $("#ZECprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZEC.USD.PRICE)
    } else {
        $("#ZECpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZEC.USD.CHANGEPCT24HOUR + "%")
        $("#ZECprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZEC.USD.PRICE)
    }
    if (data.DISPLAY.ZRX.USD.CHANGEPCT24HOUR > 0) {
        $("#ZRXpct").html("<span class=\"badge badge-pill badge-success\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZRX.USD.CHANGEPCT24HOUR + "%")
        $("#ZRXprice").html("<span class=\"badge badge-pill badge-success\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZRX.USD.PRICE)
    } else {
        $("#ZRXpct").html("<span class=\"badge badge-pill badge-danger\"><iclass=\"" +
        "fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZRX.USD.CHANGEPCT24HOUR + "%")
        $("#ZRXprice").html("<span class=\"badge badge-pill badge-danger\"><i" +
        "class=\"fas fa-arrow-alt-circle-down\"></i></span> " + data.DISPLAY.ZRX.USD.PRICE)
    }

}
