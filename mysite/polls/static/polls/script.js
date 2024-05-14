window.onload = function() {
    var svg = document.getElementById('svg-container').firstChild;
    var squares = svg.getElementsByTagName('rect');
    for (let i = 0; i < squares.length; i++) {
        var listItem = document.createElement('li');
        listItem.textContent = 'Square ' + (i + 1);
        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', function() {
            svg.removeChild(squares[i]);
            document.getElementById('square-list').removeChild(listItem);
        });
        listItem.appendChild(deleteButton);
        document.getElementById('square-list').appendChild(listItem);
    }
};

document.getElementById('add').addEventListener('click', function() {
    var svgNS = "http://www.w3.org/2000/svg";
    var rect = document.createElementNS(svgNS,'rect');
    rect.setAttributeNS(null, 'x', Math.random() * 100);
    rect.setAttributeNS(null, 'y', Math.random() * 100);
    rect.setAttributeNS(null, 'height', '10');
    rect.setAttributeNS(null, 'width', '10');
    rect.setAttributeNS(null, 'fill', 'green');
    document.getElementById('svg-container').firstChild.appendChild(rect);

    var listItem = document.createElement('li');
    listItem.textContent = 'Square ' + (document.getElementById('svg-container').firstChild.childNodes.length);
    var deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', function() {
        document.getElementById('svg-container').firstChild.removeChild(rect);
        document.getElementById('square-list').removeChild(listItem);
    });
    listItem.appendChild(deleteButton);
    document.getElementById('square-list').appendChild(listItem);
});

document.getElementById('delete').addEventListener('click', function() {
    var svg = document.getElementById('svg-container').firstChild;
    if (svg.lastChild) {
        svg.removeChild(svg.lastChild);
        var list = document.getElementById('square-list');
        list.removeChild(list.lastChild);
    }
});