$(document).ready(function() {
    var countryDropdown = $('#country');
    var cityDropdown = $('#city');

    // Dictionary with country-city mappings
    var countryCities = {
        'Thiruvananthapuram': ['Kazhakootum', 'Varkkala', ';Thamanoor'],
        'Kollam': ['Karunagappally', 'Kottarakkara', 'Ayur'],
        'Pathanamthitta': ['Adoor', 'Panthalam', 'Konni'],
        'Alappuzha': ['Kayamkulam', 'acharumood', 'kuttanad'],
        'Kottayam': ['Changanassery', 'Pala', 'Vaikom'],
        'Idukki': ['Thekkadi', 'Vagomon', 'Munnar'],
        'Eranakulam': ['Kochi', 'Mattanchery', 'Kadamakkudi'],
        'Thrissur': ['Viyyur', 'Poonkunnam', 'Cherur'],
        'Palakkad': ['Ottappalam', 'Mannarkad', 'Pattambi'],
        'Malappuram': ['Kodur', 'marayur', 'Kollur'],
        'Kozhikod': ['Payyoli', 'Mukkam', 'Vadakara'],
        'Wayanad': ['Thirunalli', 'Mananthavadi', 'Sulthan Batheri'],
        'Kannur': ['Thalasseri', 'Thalipparamb', 'Iritty'],
        'Kasargod': ['Kappil', 'Bekal', 'aaKottacheri']
    };

    // Populate country dropdown
    $.each(countryCities, function(country, cities) {
        countryDropdown.append($('<option>').text(country).attr('value', country));
    });

    // Handle country change event
    countryDropdown.change(function() {
        var selectedCountry = $(this).val();
        cityDropdown.empty();

        $.each(countryCities[selectedCountry], function(index, city) {
            cityDropdown.append($('<option>').text(city).attr('value', city));
        });
    });
    // Handle form submission
    $('#dependent-dropdown-form').on('submit', function(event) {
        event.preventDefault(); // Prevent actual form submission
        alert('Form submitted successfully!'); // Display alert message
        window.location.href = '/home'; // Redirect to home page
    });
});

