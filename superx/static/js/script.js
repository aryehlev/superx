// JavaScripts functions

// Check if item is already in cart
function addItemIfInCart(product_id, product_name, num_items){
  //test 1- console.log("yes");
  var b = false;
  var table = $('#cartbody');
  //test 2- console.log(table);
  if(table != null){
    //test 3- console.log(table[0].rows.length);
    for(var i = 0; i < table[0].rows.length; i++) {
      var id = table[0].rows[i].id;
      //test 4- console.log(id);
      if(id == product_id)
        b = true;
    }
  }
  //test 5- console.log(b);
  if(!b)
    addItem(product_id, product_name, num_items);
}

// adding Items from "myTable" table to "mycart" table
function addItem(product_id, product_name, num_items){
  req = $.ajax({
    url: "/addItem",
    method: "POST",
    data: {id: product_id, name: product_name, num_items: num_items},
    success: function (res) {
      // console.log("did it2");
      const tableBody = $('#cartbody');
      tableBody.append($(`<tr id="${product_id}">
        <td colspan="0" hidden>${product_id}</td>
        <td colspan="2">${product_name}</td>
        <td colspan="2"><input type="number" onchange="addToSession(${product_id}, this.value)" id="numItems2" value="1" min="1"></td>
        <td><button onclick="removeItem(${product_id})" type="button" class="btn btn-outline-danger">הסר מהעגלה</button></td>
        <td colspan="0"><input type="hidden" name="${product_id}"></td>
            </tr>`));
    }
  })

  req.done(function(data){
    if (data.was_city_chosen)
    {
      $('#comperbutton').removeAttr('disabled');
    }
  })
}

// function that removes table row and if there are no items in cart - disabled 'comparebutton' button
function removeItem(product_id) {
  $.ajax({
    url: "/removeItem",
    method: "POST",
    data: {id: product_id},
    success: function (res) {
      $('#' + product_id).remove();
      if ($('#cartbody tr').length === 0) {
          $("#comperbutton").attr('disabled', '');
  }
}
})
}

// live search
$(document).ready(function(e) {
    var timeout;
    var delay = 500;   // 0.5 seconds

    if ($('#cartbody tr').length === 0) {
        $("#comperbutton").attr('disabled', '');
    } else {
        $('#comperbutton').removeAttr('disabled');
    }

    $("#myInput").keypress(function(e) {
        console.log("User started typing");
        if(timeout) {
            clearTimeout(timeout);
        }
        timeout = setTimeout(function() {
            search();
        }, delay);
    });

    function search() {
        console.log("Executing search()");
        $.ajax({
        url: "/livesearch",
        method: "POST",
        data: {input: $("#myInput").val()},
        success: function (res) {
            $('#tbody').empty();
            $('#tbody').append(res);
        }
      })
    }
});

// Sending cityChoice value to the flask app using Ajax
$(document).ready(function(e) {
    var timeout;
    var delay = 1000;   // 1 second

    $("#cityChoice").keyup(function(e) {
        console.log("User started searching for city");
        if(timeout) {
            clearTimeout(timeout);
        }
        timeout = setTimeout(function() {
            citySearch();
        }, delay);
    });

    function citySearch() {
        console.log("Executing search()");
        req = $.ajax({
        url: "/city",
        method: "POST",
        data: {city: $("#cityChoice").val()},
        success: function (res) {
          if ($('#cartbody tr').length != 0)
          {
            $('#comperbutton').removeAttr('disabled');
          }
          
        }

      })
    }
});

$(document).ready(function(e) {
  $("#cityCompare").click(function(e) {
    $.ajax({
      url: "/city_search",
      method: "POST",
      success: function (res) {
        $('#cityCompare').remove();
        $( ".inner" ).append(res);
      }
    })   
  });
});

function addToSession (product_id, num_items){
    $.ajax({
        url: "/update_num_items",
        method: "POST",
        data: {id: product_id, num_items: num_items},
        success: function (res) {
            console.log("success")
        }
    })
}
