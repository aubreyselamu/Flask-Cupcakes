const BASE_URL = 'http://127.0.0.1:5000/api'

function generateCupcakeHTMLMarkup(cupcake){
    return `
    <div data-cupcake-id={cupcake.id}>
        <li>
            ${cupcake.flavor}/ ${cupcake.size} / ${cupcake.rating}
            <button class="delete-button">X</button
        </li>
        <img class="Cupcake-img"
            src="${cupcake.image}"
            alt="(no image provided)">
    </div>
  `;
}

/** show initial list of cupcakes */
async function showInitialCupcakes(){
    const response = await axios.get(`${BASE_URL}/cupcakes`)
    for(let cupcakeData of response.data.cupcakes){
        let newCupcake = generateCupcakeHTMLMarkup(cupcakeData)
        $('#cupcakes-list').append(newCupcake)
    }
}

/** handle form for adding a cupcake */
$('#add-new-cupcake').on("submit", async function(evt){
    evt.preventDefault();

    //extracting values from submitted form
    let flavor = $('#form-flavor').val()
    let size = $('#form-size').val()
    let rating = $('#form-rating').val()
    let image = $('#form-image').val()

    let data = {
        flavor,
        size,
        rating,
        image
    }

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, data)
    let newCupcake = generateCupcakeHTMLMarkup(newCupcakeResponse.data.cupcake)
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");

})

$('#cupcakes-list').on('click','.delete-button', async function(evt){
    evt.preventDefault()
    let $cupcake = $(evt.target).closest('div')
    let cupcakeId = $cupcake.attr('data-cupcake-id')
    
    await axios.delete(`${BASE_URL}/cupcakes/${cupcake.id}`)
    $cupcake.remove()
})

$(showInitialCupcakes)
