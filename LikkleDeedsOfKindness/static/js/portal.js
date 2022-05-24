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