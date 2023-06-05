document.addEventListener("DOMContentLoaded", function() {
  const addTaskForm = document.getElementById("addTaskForm");
  const taskList = document.getElementById("taskList");

  addTaskForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const taskNameInput = document.getElementById("taskName");
    const taskDescriptionInput = document.getElementById("taskDescription");

    const task = {
      name: taskNameInput.value,
      description: taskDescriptionInput.value,
      status: "Incomplete"
    };

    addTask(task);
    taskNameInput.value = "";
    taskDescriptionInput.value = "";
  });

  function addTask(task) {
    const taskElement = document.createElement("div");
    taskElement.classList.add("task");

    const nameElement = document.createElement("p");
    nameElement.textContent = "Name: " + task.name;

    const descriptionElement = document.createElement("p");
    descriptionElement.textContent = "Description: " + task.description;

    const statusElement = document.createElement("p");
    statusElement.textContent = "Status: " + task.status;

    const completeButton = document.createElement("button");
    completeButton.textContent = "Mark Complete";
    completeButton.addEventListener("click", function() {
      task.status = "Complete";
      statusElement.textContent = "Status: " + task.status;
      nameElement.classList.add("complete");
      descriptionElement.classList.add("complete");
      statusElement.classList.add("complete");
    });

    taskElement.appendChild(nameElement);
    taskElement.appendChild(descriptionElement);
    taskElement.appendChild(statusElement);
    taskElement.appendChild(completeButton);

    taskList.appendChild(taskElement);
  }
});