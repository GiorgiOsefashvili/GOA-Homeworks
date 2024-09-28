document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const clearTasksBtn = document.getElementById('clearTasksBtn');
    const taskList = document.getElementById('taskList');

    // Load tasks from localStorage
    const loadTasks = () => {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => addTaskToDOM(task.text, task.completed));
    };

    // Add task to the DOM
    const addTaskToDOM = (taskText, completed = false) => {
        const li = document.createElement('li');
        li.classList.toggle('completed', completed);

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = completed;
        checkbox.addEventListener('change', () => {
            li.classList.toggle('completed', checkbox.checked);
            updateLocalStorage();
        });

        const deleteBtn = document.createElement('button');
        deleteBtn.innerText = 'Delete';
        deleteBtn.addEventListener('click', () => {
            taskList.removeChild(li);
            updateLocalStorage();
        });

        li.appendChild(checkbox);
        li.appendChild(document.createTextNode(taskText));
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
    };

    // Update localStorage
    const updateLocalStorage = () => {
        const tasks = [];
        document.querySelectorAll('#taskList li').forEach(li => {
            const checkbox = li.querySelector('input[type="checkbox"]');
            tasks.push({
                text: li.childNodes[1].nodeValue.trim(),
                completed: checkbox.checked
            });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    // Add task event
    addTaskBtn.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            addTaskToDOM(taskText);
            taskInput.value = '';
            updateLocalStorage();
        }
    });

    // Clear all tasks
    clearTasksBtn.addEventListener('click', () => {
        taskList.innerHTML = '';
        localStorage.removeItem('tasks');
    });

    // Load tasks on page load
    loadTasks();
});
