jQuery(function(){
	    $("#select-file").change(function() { 
	      	$("#form-select-file").submit(); 
	    });
	});

    $(document).ready(function(){
	    $('.add-file').click(function() {
			if (document.getElementById('add-file').style.transform != 'translateX(125px)') {
				document.getElementById('add-file').style.transition = '1s';
		        document.getElementById('add-file').style.transform = 'translateX(125px)';
		        document.getElementById('select-file').style.transition = '1s';
		        document.getElementById('select-file').style.width = '110px';

		    } else {
		        document.getElementById('add-file').style.transform = 'translateX(0px)';
		        document.getElementById('select-file').style.width = '160px';
		    }
        });
    });
        

	$(document).ready(function(){
		$('.link').click(function() {
			var data_qid = this.dataset.qid;
			document.getElementById(data_qid).style.display = 'block';
			doc = document.getElementsByClassName(data_qid);

			for(var i = 0; i < doc.length; i++){
			    doc[i].style.display = "none";
			}

			$('.cancel').click(function() {
			    var data_qid = this.dataset.qid;
			    	
                document.getElementById(data_qid).style.display = 'none';
                doc = document.getElementsByClassName(data_qid);

				for(var i = 0; i < doc.length; i++){
				    doc[i].style.display = "block";
				}
			});
		});
	});