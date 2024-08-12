document.addEventListener('DOMContentLoaded', () => {
    fetch('results.json')
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

                for (let [step, result] of Object.entries(testResults)) {
                    const resultItem = document.createElement('div');
                    resultItem.classList.add('result-item');

                    // Desempaquetar el resultado
                    const [success, reason] = Array.isArray(result) ? result : [result, "Sin razón específica, probablemente problemas con la conexion del servidor"];
                    
                    if (success) {
                        resultItem.innerHTML = `<span>Step ${step}:</span> <span class="success">Success</span>`;
                        correctCount += 1;
                    } else {
                        resultItem.innerHTML = `<span>Step ${step}:</span> <span class="fail">Fail</span> <span class="reason" style="display:none;">(${reason})</span>`;
                        
                        // Agregar evento de clic para mostrar/ocultar la razón
                        resultItem.addEventListener('click', (event) => {
                            event.stopPropagation(); // Detener la propagación del evento de clic
                            const reasonElement = resultItem.querySelector('.reason');
                            reasonElement.style.display = reasonElement.style.display === 'none' ? 'inline' : 'none';
                        });
                    }
                    
                    testSummary.appendChild(resultItem);
                }

                const summaryItem = document.createElement('div');
                summaryItem.innerHTML = `<strong>Result of test: ${correctCount}/${testTotal}</strong>`;
                testSummary.appendChild(summaryItem);

                testItem.appendChild(testSummary);

                // Agregar un evento de clic para mostrar/ocultar el resumen del test
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
