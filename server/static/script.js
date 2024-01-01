    function uploadPDF() {

        const input = document.getElementById('pdfInput');
        const files = input.files;
        if (files.length > 0) {
            const loader = document.getElementById('loader');
            loader.classList.add('loader'); // the spinning loader

            const formData = new FormData();

            for (let i = 0; i < files.length; i++) {
                formData.append('pdfFiles', files[i]);
            }

            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML  = "";

            fetch('/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                resultDiv.innerHTML  = data.message;

                if (data.success) {
                    loader.classList.remove('loader'); // the spinning loader
                    // Enable the button after displaying the result
                    document.getElementById('downloadBtn').removeAttribute("hidden");

                }
                else {
                    document.getElementById('downloadBtn').setAttribute("hidden", "hidden");
                    loader.classList.remove('loader'); // the spinning loader
                }
            })
            .catch(error => {
                loader.classList.remove('loader'); // the spinning loader
                // Re-enable the button in case of an error
                document.getElementById('downloadBtn').disabled = false;
                document.getElementById('downloadBtn').setAttribute("hidden", "hidden");

            });
        }
    }

function downloadZIP() {

    // Fetch the PDF paths from the server
    fetch('/download-zip', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ pdfPaths: window.uploadedPDFPaths }),
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(new Blob([blob]));
        const a = document.createElement('a');
        a.href = url;
        a.download = 'generated.zip';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);

        // Re-enable the button after the download has completed
        document.getElementById('downloadBtn').disabled = false;
    })
    .catch(error => {
        console.error('Error:', error);
        // Re-enable the button in case of an error
        document.getElementById('downloadBtn').disabled = false;
    });
}
