const canvas = document.getElementById("signature-pad");
const ctx = canvas.getContext("2d");

// Clear canvas to ensure transparency at start
ctx.clearRect(0, 0, canvas.width, canvas.height);

let drawing = false;

// Mouse events
canvas.addEventListener("mousedown", () => (drawing = true));
canvas.addEventListener("mouseup", () => {
  drawing = false;
  ctx.beginPath();
});
canvas.addEventListener("mouseout", () => {
  drawing = false;
  ctx.beginPath();
});
canvas.addEventListener("mousemove", draw);

// Drawing logic for mouse
function draw(e) {
  if (!drawing) return;
  const rect = canvas.getBoundingClientRect();
  ctx.lineWidth = 2;
  ctx.lineCap = "round";
  ctx.strokeStyle = "#000";
  ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
}

// Touch support for mobile
canvas.addEventListener(
  "touchstart",
  (e) => {
    e.preventDefault();
    const touch = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    const x = touch.clientX - rect.left;
    const y = touch.clientY - rect.top;
    ctx.beginPath();
    ctx.moveTo(x, y);
    drawing = true;
  },
  { passive: false }
);

canvas.addEventListener(
  "touchmove",
  (e) => {
    e.preventDefault();
    if (!drawing) return;
    const touch = e.touches[0];
    const rect = canvas.getBoundingClientRect();
    const x = touch.clientX - rect.left;
    const y = touch.clientY - rect.top;
    ctx.lineTo(x, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y);
  },
  { passive: false }
);

canvas.addEventListener(
  "touchend",
  (e) => {
    e.preventDefault();
    drawing = false;
  },
  { passive: false }
);

canvas.addEventListener(
  "touchcancel",
  (e) => {
    e.preventDefault();
    drawing = false;
  },
  { passive: false }
);

// Clear signature
function clearSignature() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
}

// Prepare signature image as data URL for submission
function prepareSignature() {
  const dataURL = canvas.toDataURL("image/png");
  document.getElementById("signature_data").value = dataURL;
}
