const taskForm = document.getElementById('task-form')
const taskInput = document.getElementById('task-input')
const taskList = document.getElementById('task-list')

taskForm.addEventListener('submit', function(event){
    event.preventDefault()
    addTask()
})

function addTask (){
    const taskText = taskInput.value.trim()
    console.log(taskInput.value.trim());
    if (taskText !== ''){
        const li = document.createElement('li')
        li.innerHTML = `
        <span>${taskText}</span>
        <button class="delete">Excluir</button>
        `
        taskList.appendChild(li)
        taskInput.value = ""
    
    const deleteButton = li.querySelector('.delete')
    deleteButton.addEventListener('click', function(){
    li.remove()
    })
    }
}   