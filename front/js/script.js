fetch("http://127.0.0.1:8000/alumnes/llista")
    .then(response => {
        console.log("Resposta del servidor:", response);
        if (!response.ok) {
            console.error("Error a la resposta del servidor", response.status);
            throw new Error("Error a la resposta del servidor");
        }
        return response.json();
    })
    .then(data => {
        console.log("Dades rebudes:", data);

        if (!Array.isArray(data)) {
            throw new Error("La resposta no és una llista d'alumnes");
        }

        const alumnesTableBody = document.querySelector("#tablaAlumne tbody");
        if (!alumnesTableBody) {
            throw new Error("No s'ha trobat la taula o el tbody a l'HTML");
        }

        alumnesTableBody.innerHTML = "";

        data.forEach(alumne => {
            console.log("Alumne:", alumne);

            const row = document.createElement("tr");

            const nomAluCell = document.createElement("td");
            nomAluCell.textContent = alumne.NomAlumne || 'Desconegut';
            row.appendChild(nomAluCell);

            const cicleAluCell = document.createElement("td");
            cicleAluCell.textContent = alumne.cicle || 'Desconegut';
            row.appendChild(cicleAluCell);

            const cursAluCell = document.createElement("td");
            cursAluCell.textContent = alumne.curs || 'Desconegut';
            row.appendChild(cursAluCell);

            const grupAluCell = document.createElement("td");
            grupAluCell.textContent = alumne.grup || 'Desconegut';
            row.appendChild(grupAluCell);

            const descAulaCell = document.createElement("td");
            descAulaCell.textContent = alumne.DescAula || 'Desconegut';
            row.appendChild(descAulaCell);

            alumnesTableBody.appendChild(row);
        });
    })
    .catch(error => {
        console.error("Error capturat:", error);
        alert("Error al carregar la llista d'alumnes");
    });
