try {
    let a;
    a = 5 / 0;
}
catch {
    paragraph.innerHTML = "Došlo k chybě";
}

throw Error;