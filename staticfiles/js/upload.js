document.addEventListener("DOMContentLoaded", function () {
  const dropArea = document.getElementById("uploadForm");
  const fileInput = document.getElementById("fileInput");
  const fileNameDisplay = document.getElementById("fileName");

  if (!dropArea || !fileInput || !fileNameDisplay) return;

  dropArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropArea.classList.add("bg-gray-300");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("bg-gray-300");
  });

  dropArea.addEventListener("drop", (e) => {
    e.preventDefault();
    dropArea.classList.remove("bg-gray-300");

    if (e.dataTransfer.files.length) {
      fileInput.files = e.dataTransfer.files;
      fileNameDisplay.textContent = `Selected: ${fileInput.files[0].name}`;
    }
  });

  fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
      fileNameDisplay.textContent = `Selected: ${fileInput.files[0].name}`;
    }
  });
});
