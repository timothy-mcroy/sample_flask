$(document).ready(function(){
  $("form input").on("focusout", function(e){
    tmp = $(e.currentTarget);
    id = tmp.attr("id");
    val = tmp.val();
    $.post({
      url: '/updatevals',
      data: {
        id: id,
        val: val,
      },
    }).done( function(data) {
      console.log("#winning");5
      for (id in data){
        console.log("id " + id+" and data[id]" + data[id]);
        $("#"+id).val(data[id]);
      }
    });
  });
});
