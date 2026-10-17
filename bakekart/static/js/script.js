// some scripts

// jquery ready start
$(document).ready(function() {
	// jQuery code


    /* ///////////////////////////////////////

    THESE FOLLOWING SCRIPTS ONLY FOR BASIC USAGE, 
    For sliders, interactions and other

    */ ///////////////////////////////////////
    

	//////////////////////// Prevent closing from click inside dropdown
    $(document).on('click', '.dropdown-menu', function (e) {
      e.stopPropagation();
    });


    $('.js-check :radio').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $('input[name='+ check_attr_name +']').closest('.js-check').removeClass('active');
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');

        } else {
            item.removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });


    $('.js-check :checkbox').change(function () {
        var check_attr_name = $(this).attr('name');
        if ($(this).is(':checked')) {
            $(this).closest('.js-check').addClass('active');
           // item.find('.radio').find('span').text('Add');
        } else {
            $(this).closest('.js-check').removeClass('active');
            // item.find('.radio').find('span').text('Unselect');
        }
    });



	//////////////////////// Bootstrap tooltip
	if($('[data-toggle="tooltip"]').length>0) {  // check if element exists
		$('[data-toggle="tooltip"]').tooltip()
	} // end if




    
}); 
// jquery end


document.addEventListener("DOMContentLoaded", function () {
    const servingLink = document.getElementById("serving-info-link");
    const servingPanel = document.getElementById("serving-panel");
    const servingOverlay = document.getElementById("serving-overlay");
    const closeButton = document.getElementById("close-serving-panel");
    const servingInfo = document.getElementById("serving-info");

    const servingSizes = {
        "0.5": "4 - 5 People",
        "1": "8 - 10 People",
        "1.5": "12 - 14 People",
        "2": "18 - 20 People",
        "4": "36 - 46 People"
    };

    document.querySelectorAll('input[name="weight"]').forEach(function (input) {
        input.addEventListener("change", function () {
            if (servingInfo) {
                servingInfo.textContent = servingSizes[this.value];
            }
        });
    });

    if (!servingLink || !servingPanel || !servingOverlay || !closeButton) {
        return;
    }

    function openServingPanel(event) {
        event.preventDefault();
        servingPanel.classList.add("active");
        servingOverlay.classList.add("active");
        document.body.classList.add("serving-panel-open");
    }

    function closeServingPanel() {
        servingPanel.classList.remove("active");
        servingOverlay.classList.remove("active");
        document.body.classList.remove("serving-panel-open");
    }

    servingLink.addEventListener("click", openServingPanel);
    closeButton.addEventListener("click", closeServingPanel);
    servingOverlay.addEventListener("click", closeServingPanel);

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            closeServingPanel();
        }
    });
});
