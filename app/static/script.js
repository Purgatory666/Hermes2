
// --- FULL JS FROM ORIGINAL index.html ---
const mainInput = document.getElementById('mainInput');
const inputArrow = document.getElementById('inputArrow');
const logo = document.querySelector('.logo');
const featuresBar = document.getElementById('featuresBar');
const targetLanguageValue = document.getElementById('targetLanguageValue');
const languageSearch = document.getElementById('languageSearch');
const writingStyleValue = document.getElementById('writingStyleValue');
const originalityValue = document.getElementById('originalityValue');
const dialectInput = document.getElementById('dialectInput');
const creativeIntentInput = document.getElementById('creativeIntentInput');
let selectedStyle = '';
let selectedOriginality = [];

mainInput.addEventListener('focus', () => {
	featuresBar.classList.add('visible');
});
mainInput.addEventListener('blur', () => {
	if (!mainInput.value) {
		featuresBar.classList.remove('visible');
	}
});
mainInput.addEventListener('input', () => {
	if (mainInput.value.trim()) {
		inputArrow.classList.add('visible');
	} else {
		inputArrow.classList.remove('visible');
	}
});
const originalityCheckboxes = document.querySelectorAll('.checkbox-item input');
originalityCheckboxes.forEach(checkbox => {
	checkbox.addEventListener('change', () => {
		const value = checkbox.getAttribute('data-originality');
		if (checkbox.checked) {
			selectedOriginality.push(value);
		} else {
			selectedOriginality = selectedOriginality.filter(item => item !== value);
		}
		if (selectedOriginality.length === 0) {
			originalityValue.textContent = 'Select Options ▼';
		} else if (selectedOriginality.length === 1) {
			originalityValue.textContent = selectedOriginality[0] + ' ▼';
		} else {
			originalityValue.textContent = selectedOriginality.length + ' selected ▼';
		}
	});
});
languageSearch.addEventListener('input', function() {
	const filter = this.value.toLowerCase();
	const links = document.querySelectorAll('.target-language .dropdown-content a');
	links.forEach(link => {
		const text = link.textContent.toLowerCase();
		if (text.includes(filter)) {
			link.style.display = 'block';
		} else {
			link.style.display = 'none';
		}
	});
});
targetLanguageValue.addEventListener('click', function() {
	const dropdown = this.nextElementSibling;
	dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
});
const languageLinks = document.querySelectorAll('.target-language .dropdown-content a');
languageLinks.forEach(link => {
	link.addEventListener('click', function(e) {
		e.preventDefault();
		const lang = this.getAttribute('data-lang');
		targetLanguageValue.textContent = `${lang} ▼`;
		this.closest('.dropdown-content').style.display = 'none';
	});
});
const writingStyleDropdown = document.querySelector('.style .dropdown-content');
writingStyleValue.addEventListener('click', function() {
	writingStyleDropdown.style.display = writingStyleDropdown.style.display === 'block' ? 'none' : 'block';
});
const styleLinks = document.querySelectorAll('.style .dropdown-content a');
styleLinks.forEach(link => {
	link.addEventListener('click', function(e) {
		e.preventDefault();
		const style = this.getAttribute('data-style');
		const displayText = style === '' ? 'None' : style.charAt(0).toUpperCase() + style.slice(1);
		writingStyleValue.textContent = `${displayText} ▼`;
		writingStyleDropdown.style.display = 'none';
		selectedStyle = style;
	});
});
document.addEventListener('click', function(e) {
	if (!e.target.closest('.style')) {
		writingStyleDropdown.style.display = 'none';
	}
	if (!e.target.closest('.target-language')) {
		document.querySelector('.target-language .dropdown-content').style.display = 'none';
	}
});
inputArrow.addEventListener('click', () => {
	const text = mainInput.value.trim();
	if (!text) return;
	document.getElementById('loading').classList.add('visible');
	document.getElementById('resultContainer').classList.remove('visible');
	const targetLang = targetLanguageValue.textContent.replace(' ▼', '');
	const writingStyle = selectedStyle;
	const dialect = dialectInput.value.trim();
	const creativeIntent = creativeIntentInput.value.trim();
	const model = 'llama3:8b';
	const formData = new FormData();
	formData.append('text', text);
	formData.append('mode', 'translate');
	formData.append('target_lang', targetLang);
	formData.append('writing_style', writingStyle);
	formData.append('originality', JSON.stringify(selectedOriginality));
	if (dialect) formData.append('dialect', dialect);
	if (creativeIntent) formData.append('creative_intent', creativeIntent);
	formData.append('model', model);
	fetch('/translate', {
		method: 'POST',
		body: formData,
		headers: {
			'X-Requested-With': 'XMLHttpRequest'
		}
	})
	.then(response => response.json())
	.then(data => {
		if (data.error) {
			throw new Error(data.error);
		}
		document.getElementById('loading').classList.remove('visible');
		document.getElementById('translationResult').textContent = data.output;
		document.getElementById('resultContainer').classList.add('visible');
	})
	.catch(error => {
		console.error('Error:', error);
		document.getElementById('loading').classList.remove('visible');
		document.getElementById('translationResult').textContent = 'Error: ' + error.message;
		document.getElementById('resultContainer').classList.add('visible');
	});
});
mainInput.addEventListener('keydown', (e) => {
	if (e.key === 'Enter' && !e.shiftKey) {
		e.preventDefault();
		inputArrow.click();
	}
});
