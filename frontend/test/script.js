document.addEventListener('DOMContentLoaded', () => {
    fetch('../../results.json')
        .then(response => response.json())
        .then(results => {
            const resultsContainer = document.getElementById('results');
            const totalContainer = document.getElementById('total');
            let overallTotal = 0;
            let overallCorrect = 0;

            for (let [testName, testResults] of Object.entries(results)) {
                let correctCount = 0;
                let testTotal = Object.keys(testResults).length;

                const testItem = document.createElement('div');
                testItem.classList.add('test-item');
                testItem.innerHTML = `<h2>${testName}</h2>`;

                const testSummary = document.createElement('div');
                testSummary.classList.add('test-summary');
                testSummary.style.display = 'none'; // Oculto por defecto
                let count = 0;
                for (let [step, result] of Object.entries(testResults)) {
                    count += 1;
                    const resultItem = document.createElement('div');
                    resultItem.classList.add('result-item');
                    resultItem.innerHTML = `<span>Step ${step}:</span> <span>${result ? 'Success' : 'Fail'}</span>`;
                    testSummary.appendChild(resultItem);

                    if (result) correctCount += 1;
                    if (count === testTotal) {
                        resultItem.innerHTML = `<strong> ${"Result of test"}: ${correctCount}/${testTotal}</strong>`;
                        testSummary.appendChild(resultItem);
                    }
                }


                testItem.appendChild(testSummary);

                // Agregar un evento de clic para mostrar/ocultar el resumen
                testItem.addEventListener('click', () => {
                    testSummary.style.display = testSummary.style.display === 'none' ? 'block' : 'none';
                });

                // Agregar el test al contenedor de resultados
                resultsContainer.appendChild(testItem);

                // Contabilizar el total general
                overallTotal += testTotal;
                overallCorrect += correctCount;
            }

            // Mostrar el total general
            totalContainer.textContent = `Total: ${overallCorrect}/${overallTotal}`;
        })
        .catch(error => console.error('Error loading results:', error));
});
