const chatInput = document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chatbox");

let userMessage;
const inputInitHeight = chatInput.scrollHeight;

// Function to create a chat bubble
const createChatLi = (message, className) => {
  const chatLi = document.createElement("li");
  chatLi.classList.add("chat", className);
  let chatContent =
    className === "outgoing"
      ? `<p></p>`
      : `<span><i class="fa-solid fa-people-roof"></i></span> <p></p>`;
  chatLi.innerHTML = chatContent;
  chatLi.querySelector("p").textContent = message;
  return chatLi;
};

// Function to generate response from Django backend
const generateResponse = (incomingChatLi) => {
  const messageElement = incomingChatLi.querySelector("p");

  fetch("/chat/api/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: userMessage }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.reply) {
        messageElement.textContent = data.reply;
      } else {
        messageElement.textContent = "Oops! Something went wrong.";
      }
    })
    .catch((error) => {
      messageElement.classList.add("error");
      messageElement.textContent =
        "Oops! Something went wrong. Please try again.";
    })
    .finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
};

// Handles when user sends a message
const handleChat = () => {
  userMessage = chatInput.value.trim();
  if (!userMessage) return;

  // Reset input field
  chatInput.value = "";
  chatInput.style.height = `${inputInitHeight}px`;

  // Show user's message
  chatbox.appendChild(createChatLi(userMessage, "outgoing"));
  chatbox.scrollTo(0, chatbox.scrollHeight);

  // Show placeholder for bot reply
  setTimeout(() => {
    const incomingChatLi = createChatLi("Thinking...", "incoming");
    chatbox.appendChild(incomingChatLi);
    chatbox.scrollTo(0, chatbox.scrollHeight);
    generateResponse(incomingChatLi);
  }, 600);
};

// Dynamic resizing of textarea
chatInput.addEventListener("input", () => {
  chatInput.style.height = `${inputInitHeight}px`;
  chatInput.style.height = `${chatInput.scrollHeight}px`;
});

// Send message on Enter (without Shift) on desktop
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
    e.preventDefault();
    handleChat();
  }
});

// Send message on click
sendChatBtn.addEventListener("click", handleChat);
