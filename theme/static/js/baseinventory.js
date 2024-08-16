document.getElementById('togglefish').addEventListener('click', function() {
    var toggleDiv = document.getElementById('filters');
    toggleDiv.classList.toggle('hidden');
});

document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".filter-btn:not(.dropdown)");

    buttons.forEach(button => {
        button.addEventListener("click", function() {
            this.classList.toggle("bg-violet-500");
            this.classList.toggle("bg-violet-300");

            const kitType = this.getAttribute("data-kit");
            const selectedTable = document.getElementById(`${kitType}-tablediv`);

            if (selectedTable) {
                selectedTable.classList.toggle("hidden");
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const tables = document.querySelectorAll("table:not(.dropdown)");

    tables.forEach(table => {
        const headers = table.querySelectorAll('.sortable-header');

        headers.forEach(header => {
            // Add a span to each header for the arrow
            const arrow = document.createElement('span');
            arrow.classList.add('arrow');
            header.appendChild(arrow);

            header.addEventListener('click', function() {
                const isAscending = header.classList.contains('sorted-asc');

                // Remove arrows from all headers
                headers.forEach(h => {
                    h.classList.remove('sorted-asc', 'sorted-desc');
                    const arrowInHeader = h.querySelector('.arrow');
                    if (arrowInHeader) arrowInHeader.textContent = ''; // Clear arrow
                });

                // Toggle sorting direction for the clicked header
                header.classList.toggle('sorted-asc', !isAscending);
                header.classList.toggle('sorted-desc', isAscending);

                // Set the arrow based on sorting direction
                if (!isAscending) {
                    arrow.textContent = '🔼'; // Up Arrow for ascending
                } else {
                    arrow.textContent = '🔽'; // Down Arrow for descending
                }

                const rows = Array.from(table.querySelectorAll('tbody tr'));
                const columnIndex = Array.prototype.indexOf.call(header.parentNode.children, header);

                // Sort rows
                rows.sort((a, b) => {
                    const aText = a.cells[columnIndex].textContent;
                    const bText = b.cells[columnIndex].textContent;
                    if (!isNaN(aText) && !isNaN(bText)) {
                        return isAscending ? parseFloat(bText) - parseFloat(aText) : parseFloat(aText) - parseFloat(bText);
                    } else {
                        return isAscending ? bText.localeCompare(aText) : aText.localeCompare(bText);
                    }
                });

                // Append sorted rows
                rows.forEach(row => table.querySelector('tbody').appendChild(row));
            });
        });
    });
});