import SwiftUI

struct ContentView: View {
    @State var todos = ["Item 1", "Item 2", "Item 3"]
    @State var newTodo = ""
    
    var body: some View {
        VStack {
            HStack {
                TextField("New Todo", text: $newTodo)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                Button(action: {
                    todos.append(newTodo)
                    newTodo = ""
                }) {
                    Text("Add")
                }
            }
            
            List(todos, id: \.self) { todo in
                Text(todo)
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}