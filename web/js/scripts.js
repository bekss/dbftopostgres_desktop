// Чтобы получить данные Postgresql
async function total_psql() {
    let username = document.getElementById('psqlusername').value
    let password = document.getElementById('psqlpassword').value
    let host = document.getElementById('psqlhost').value
    let database = document.getElementById('psqldatabase').value
    // await alert(username + password + host + database)
    await eel.data_psql(username, password, host, database)
}

//для обратного отзыва из банка
async function reverse_info(info, namesql) {
    let err = 'Данные введены не правильно повторите еще раз';
    let succ = 'Успешно подключено к ' + namesql;
    // alert(typeof(info))
    document.getElementById("connect_info").style.display = "block";
    if (info == 'False') {
        document.getElementById("connect_info").innerHTML = err;
    } else {
        document.getElementById("connect_info").innerHTML = succ;
        work_event();
    }
}

eel.expose(reverse_info, 'reverse_info')

//Для файла
function click_file() {
    eel.chosed_file();
    if (true)
        document.getElementById("file").style.display = "block";
};

function set_file(file) {
    document.getElementById("files_name").innerHTML = file;
}

eel.expose(set_file, 'set_file');

//Для теста
function setLoading(currentFase) {
    alert(currentFase)
}

eel.expose(setLoading, 'setLoading')

function test() {
    eel.load_program();
}

//Для папки
function name_file(some) {
    document.getElementById("folder_name").innerHTML = some;
}

eel.expose(name_file, 'name_file')

function click_folder() {
    a = eel.chosed_files()
    if (a) {
        document.getElementById("list_name").style.display = "block";
    }
}

async function work_event() {
    document.getElementById("signal").style.display = "block";
}

//Для selecter чтобы получить значения
// function getSelectValue(sql) {
//     let selectedValue = document.getElementById('options').value;
//     if (selectedValue!= '- - - Выберите базу данных - - -'){
//         alert(selectedValue);
//         sql(selectedValue);
//     }
//     // else
//     //     selectedValue.value = this.options[this.selectedIndex].value;
// }
//


// function connect_sql(sql_name) {
//     if (sql_name =='msql'){
//         eel.sql_con(sql_name)
//     }
//     if (sql_name=='postgresql'){
//         eel.psql_con(sql_name)
//     }
// }

function set_sql_data() {
    let selectedValue = document.getElementById('options').value;
    if (selectedValue == 'msql') {

        alert('Вы выбрали ' + selectedValue);
        // sql(selectedValue);
        eel.msql_conn();
    }
    if (selectedValue == 'postgresql') {
        alert('Вы выбрали ' + selectedValue);
        // sql(selectedValue);
        eel.psql_conn();
    }
}