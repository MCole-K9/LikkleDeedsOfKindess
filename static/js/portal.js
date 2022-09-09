function goToLocation(url) { 
    location.href = url;
}


const container = document.getElementById("preview-caption");
const fileInput = document.getElementById("project_images");

function addCaption(){

    files = fileInput.files;

    Array.from(files).forEach((image, index) => {

        let div = document.createElement("div");
        div.setAttribute("class", " card col-12 col-lg-6  p-2");

        let img = document.createElement("img");

        img.setAttribute("class", "img img-responsive card-img-top");
        img.setAttribute("style", "object-fit: cover; max-height: 200px; max-width: 100%");

        let capLabel = document.createElement("label");
        capLabel.innerText = "Caption";
        capLabel.setAttribute("for", "caption"+index);
        capLabel.setAttribute("class", "form-label mt");

        let captionInput = document.createElement("input");
        
        Object.assign(captionInput, {
            type: "text", 
            id: "caption"+index,
            name: "caption"+index,

        });
        captionInput.setAttribute("class", "form-control" );
        
        
        container.appendChild(div);

        let fileReader = new FileReader();

        fileReader.onload = ()=>{
            img.setAttribute("src", fileReader.result);
            div.appendChild(img);
            div.appendChild(capLabel);
            div.appendChild(captionInput);
        };

        fileReader.readAsDataURL(image);

    });
}
function handleEditClick(imageUrl, imgCaption, postURL){
    

    img = document.getElementById("imgEdit");
    img.setAttribute("src", imageUrl);

    $("#caption").val(imgCaption)
    
    imgForm = document.getElementById("imgForm");
    imgForm.setAttribute("action", postURL);
    
}

function handleAddClick(postURL){
    //If img was an image was edited then the image will still be visible in the modal
    img = document.getElementById("imgEdit");
    img.setAttribute("src", "");

    imgForm = document.getElementById("imgForm");
    imgForm.setAttribute("action", postURL);
    
}

$("#file_input").on("change", (event)=>{

    
    let img = document.getElementById("imgEdit");

    let files = event.target.files;

    let fileReader = new FileReader();

    fileReader.onload = ()=>{
        
        img.setAttribute("src", fileReader.result);
        
    };
    fileReader.readAsDataURL(files[0]);
});

function handleDelete(requestUrl){

    document.getElementById("delete_link").setAttribute("href", requestUrl);
}

//Toggles sidebar
document.getElementById("toggle-btn").addEventListener("click", function(){

    document.getElementById("side-bar").classList.toggle("active")
})