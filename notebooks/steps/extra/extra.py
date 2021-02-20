from IPython.core.display import HTML
from IPython.display import Image,display


toggle_code_str = '''
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Toggle Code"></form>
'''
toggle_code_prepare_str = '''
	<script>
	function code_toggle() {
	    if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
	        $('div.cell.code_cell.rendered.selected div.input').hide();
	    } else {
	        $('div.cell.code_cell.rendered.selected div.input').show();
	    }
	}
	</script>

'''

display(HTML(toggle_code_prepare_str + toggle_code_str))

def toggle_code():
	display(HTML(toggle_code_str))
		
#display(Image(filename='.img/logoev.jpg',width = 1000,height = 1000))
