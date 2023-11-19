import lib_dzne_filedata as _fd
import handle_blastn as _handle_blastn


def get_cline(prog, **kwargs):
    cline = _handle_blastn.Cline(cmd=prog, **kwargs)
    return list(cline)

def parse(text):
    summary = _handle_blastn.Summary.from_text(text)
    data = vars(summary)
    store = {k.replace('_', '-'):v for k,v in data.items()}
    ans = _fd.TOMLData(store)
    return ans
